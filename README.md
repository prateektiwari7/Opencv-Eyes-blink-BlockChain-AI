# Opencv-Eyes-blink-BlockChain-AI

To run this make sure you have all Opencv Environment set up if not please follow opencv instruction.

Note Make sure you have shape shape_predictor_68_face_landmarks.dat file if you dont have please download it from below link

https://drive.google.com/file/d/1lzXTNebqOir21s-jWMxph2SxyS9Jm85M/view?usp=sharing

then the commands are as like 

y $ workon cv
(cv) /Desktop/Opencv-Eyes-blink-BlockChain_AI $ python json_io.py 
 * Serving Flask app "json_io" (lazy loading)
 * Environment: production
   WARNING: Do not use the development server in a production environment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://0.0.0.0:5010/ (Press CTRL+C to quit)
127.0.0.1 - - [08/Jun/2018 09:44:37] "GET /output?output HTTP/1.1" 200 -
127.0.0.1 - - [08/Jun/2018 09:45:03] "GET /output?output HTTP/1.1" 200 -
127.0.0.1 - - [08/Jun/2018 09:53:32] "GET /output?output HTTP/1.1" 200 -
127.0.0.1 - - [08/Jun/2018 09:53:37] "POST /output1 HTTP/1.1" 200 -
127.0.0.1 - - [08/Jun/2018 09:53:47] "GET /output?output HTTP/1.1" 200 -
127.0.0.1 - - [08/Jun/2018 09:53:50] "POST /output1 HTTP/1.1" 200 -


Run the new cmd and type 

(cv)  ~/Documents/hacthron-face-detection/facial-landmarks $ python detect_blink.py --shape-predictor shape_predictor_68_face_landmarks.dat 
{"make":[{"count":"start"},{"count":"0"},{"count":"0"}]}

[INFO] loading facial landmark predictor...
[INFO] starting video stream thread...
(cv)  ~/Documents/hacthron-face-detection/facial-landmarks $ 


you will see screen like as 


