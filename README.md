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
#### Observations
		- Huv outperforms rgb
		- Not descaling performs worse
		- 128 out performs 64 batch
		- Using only top 2/3rd of image gives better loss


