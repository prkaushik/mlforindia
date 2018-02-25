import boto3
import json

rek = boto3.client('rekognition') # Setup Rekognition
s3 = boto3.resource('s3') # Setup S3
print("Getting Image")

image = s3.Object('peepaal-facedetect','trumprecognition.png') # Get an Image from S3
img_data = image.get()['Body'].read() # Read the image

print("Image retrieved")
print("Sending to Rekognition")

# Detect the items in the image
print("Image retrieved")
print("Sending to Rekognition")

results = rek.detect_faces(
    Image={
        'Bytes': img_data

    },
    Attributes=['ALL']
)



for faceDetail in results['FaceDetails']:
        print('The detected face is between ' + str(faceDetail['AgeRange']['Low'])
              + ' and ' + str(faceDetail['AgeRange']['High']) + ' years old')
        #print('Here are the other attributes:')
        #print(json.dumps(faceDetail, indent=4, sort_keys=True))

for faceDetail in results['FaceDetails']:
    msg = "I found a {gender} who is {emot}".format(gender=faceDetail['Gender']['Value'], emot=faceDetail['Emotions'][0]['Type'].lower())
    if faceDetail['Smile']['Value'] is False:
        msg += " but they are not smiling"
    else:
        msg += " and they are smiling"
    print(msg)


# Print the result
#print(json.dumps(results['Labels'],indent=2))


#for face in results["FaceDetails"]:
#    msg = "I found a {gender} who is {emot}".format(gender=face['Gender']['Value'], emot=face['Emotions'][0]['Type'].lower())

#    if face['Smile']['Value'] is False:
#        msg += " but they are not smiling"
#    else:
#        msg += " and they are smiling"
#    print(msg)