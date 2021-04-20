# AutonomousCars

## Notes from tweaking models

### Speed model
#### Runs and loss
	- Using image descaled by 1/2 and huv colour space
		○ Val_loss = 0.1379
	- Using top 2/3rds of image descale fx,y = 0.6 and RGB, batch=128
		○ - loss: 0.1258 - accuracy: 0.9652
	- Using top 2/3rds of image descale fx,y = 0.6 and huv, batch=64
		○ - loss: 0.1150 - accuracy: 0.9594
	- Using top 2/3rds of image descale =1 and huv, batch=64
		○ - loss: 0.1191 - accuracy: 0.9623
	- Using top 2/3rds of image descale =0.7 and huv, batch=64
		○ loss: 0.1142 - accuracy: 0.9601
	- Using top 2/3rds of image descale =0.8 and huv, batch=64
		○ loss: 0.1403 - accuracy: 0.9688
	- Using top 2/3rds of image descale =0.7 and huv, batch=128
		○ loss: 0.1071 - accuracy: 0.9604
	- Using full of image descale =0.6 and RGB, batch=128
		○ loss: 0.1144 - accuracy: 0.9552
	- Using full of image descale =0.6 and RGB, batch=32
		○ Ram problems
	- Using full image descale = 0.5 and RGB batch = 128
		○ loss: 0.1339 - accuracy: 0.9536
	- Using full image descale = 0.5 and RGB batch = 32
		○ loss: 0.1195 - accuracy: 0.9601
	- Using full image descale = 0.5 and HUV batch = 32
		○ -loss: 0.1502 - accuracy: 0.9580
	- Using top 2/3rds of image descale =0.7 and huv, batch=32
		○ loss: 0.1074 - accuracy: 0.9659
	- Using full image, descale = 0.4 and huv, batch=32
		○ loss: 0.0985 - accuracy: 0.9703

#### Observations
	- Huv outperforms rgb
	- Not descaling performs worse
	- 32 outperforms both 128 out performs 64 batch
	- Using top 2/3rd is better
	- Using augmentation to increase the size of the 0 speed data reduces the model accuracy!

#### Submissions

##### One
- Loss = 0.04006
- Speed = Using top 2/3rds of image descale =0.7 and huv, batch=32
- Angle = Normal Nvidia

##### Two
- Loss = 
- Speed = Using full image, descale = 0.4, huv, batch=32, hard coded red light detection
- Angle = Normal Nvidia

			
			

