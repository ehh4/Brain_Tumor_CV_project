## User Stories

### User 1: Researchers
Understanding how current technology can predict severity of brain tumor from early-stage brain tumor imaging.
Through website/dashboard, by uploading patient brain images, researchers will get a prediction of the severity of the brain tumor. Further research can be done to increase accuracy and/or add new features
Would be interested in the code too: add more train/test data (more brain images); update algorithms; make additional code iterations as scope increases. 



### User 2: Patient
Cyndi just received her diagnosis with a brain tumor at the age of 30. She received her MRI results that showed a tumor in the early stage of development. Instead of waiting for more information from the doctor, she would like to know more about her diagnosis. What’s the size of the tumor? What’s the severity of her condition?


### User 3:Doctors
Jane is a doctor.

Jane wants to verify that she’s correctly identified the tumor region.

She wants to submit a brain scan and have the predicted tumor size and predicted severity annotated. 

She wants to supplement her own expertise with a tool that will confirm whether her own analysis is valid.

Jane’s doesn’t have technical expertise and wants an easy-to-use interface and a simple output that gives essential information in a clean format.


## Use Case

### Objective: System uploads an image and it returns the annotated scan

User: Selects “upload” image
System: [verifies image is the correct filetype]
[if correct] [verifies image is able to be scanned]
[if image is an acceptable brain scan] continue with analysis…
[if image is unable to scan] display “sorry we don’t currently accept that image type”
[if incorrect filetype] display “sorry, this file has an incorrect filetype”

… assuming brain scan is valid and region and severity annotation is returned …
System: “Processing complete - now showing results” [return results]


### Objective: User is interested in learning more about the tool

User: [Clicks “Learn More” tab]
System: [Returns prompt] “Would you like to learn more about image segmentation or our current model?”
User: [Selects one]

