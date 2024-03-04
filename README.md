# AWS-Regex-Matching-Web-App

## Hosting the web app on AWS
Step 1: Connect to instance
![alt text](https://github.com/VishalDeoPrasad/Data-Scientist-Intern/blob/main/image/image-51.png)
![alt text](https://github.com/VishalDeoPrasad/Data-Scientist-Intern/blob/main/image/image-52.png)

Step2: Go to app folder and start `CMD`
![alt text](https://github.com/VishalDeoPrasad/Data-Scientist-Intern/blob/main/image/image-53.png)
![alt text](https://github.com/VishalDeoPrasad/Data-Scientist-Intern/blob/main/image/image-54.png)

Step 3: `SSH` - use the key and enter into server <br>
`SSH -i 'key' REMOTE_SERVER`
![alt text](https://github.com/VishalDeoPrasad/Data-Scientist-Intern/blob/main/image/image-55.png)
![alt text](https://github.com/VishalDeoPrasad/Data-Scientist-Intern/blob/main/image/image-56.png)
![alt text](https://github.com/VishalDeoPrasad/Data-Scientist-Intern/blob/main/image/image-57.png)

step 4: copy all templates and app file to single folder.
![alt text](https://github.com/VishalDeoPrasad/Data-Scientist-Intern/blob/main/image/image-58.png)

step 5: create dependecy text file
![alt text](https://github.com/VishalDeoPrasad/Data-Scientist-Intern/blob/main/image/image-59.png)
![alt text](https://github.com/VishalDeoPrasad/Data-Scientist-Intern/blob/main/image/image-60.png)

Step 6: Transfer the templates and app. `SCP`: secure copy using key. `no need of transfering 'env' and 'key'` <br>
`scp -r -i 'key' REMOTE-SERVER:~/`
![alt text](https://github.com/VishalDeoPrasad/Data-Scientist-Intern/blob/main/image/image-28.png)
__cmd:__ `scp -r -i "flask_deployment_jan_internship_24.pem" webapp ubuntu@ec2-3-83-244-219.compute-1.amazonaws.com:~/`
![alt text](https://github.com/VishalDeoPrasad/Data-Scientist-Intern/blob/main/image/image-62.png)
![alt text](https://github.com/VishalDeoPrasad/Data-Scientist-Intern/blob/main/image/image-63.png)

Step 7 : Login to server and verify the copying. <br>
__cmd__: `ssh -i "flask_deployment_jan_internship_24_key.pem" ubuntu@ec2-3-83-244-219.compute-1.amazonaws.com`
![alt text](https://github.com/VishalDeoPrasad/Data-Scientist-Intern/blob/main/image/image-64.png)

Step 8: Update OS and install dependency 
1. `sudo apt update`: download all package
2. `sudo apt upgrade`: install all package
3. `sudo apt install python3`: install python3
4. `sudo apt install python3-pip`: install pip

step 9: Run and test the application
1. fix code 
    ```python
    app.run(host='0.0.0.0', port=5000)
    ```
2. go to instance and find public ip:
![alt text](https://github.com/VishalDeoPrasad/Data-Scientist-Intern/blob/main/image/image-65.png)
3. run the program in the background
no hang-up: 
    - `python3 app.py` : hang-up
    - `nohup python3 app.py &` : provide terminal use
    - `nohup python3 app.py` <br>
4. to see the running program `top -u $USER`
5. stop the running program
kill <Process ID(PID)>: 
    - `kill 1377` nomally kill 
    - `kill -9 1377` forcefully kill
image\
