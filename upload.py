import boto3



s3 = boto3.resource('s3')


# Get list of objects for indexing


images=[('ein1.jpg','Albert Einstein'),
      
('ein2.jpg','Albert Einstein'),
      
('ein3.jpg','Albert Einstein')
,
('darwin.jpg','Darwin')
   ,
('Lab.jpg','Labby')
  ,
('lab2.jpg','Labby')
    ]



# Iterate through list to upload objects to S3   


for image in images:
    
	file = open(image[0],'rb')
    
	object = s3.Object('peepaal-facedetect','index/'+ image[0])
    
	ret = object.put(Body=file,
Metadata={'FullName':image[1]}
                   
 )