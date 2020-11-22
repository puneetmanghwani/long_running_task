## Docker Image - docker run -p 8010:8000 puneetmanghwani/atlan

## APIs
   1. **API to Upload CSV file**
   
   `/data/uploadfile/`  
   Method: POST  
   Server receives file with key as `file`  
   The unique Task ID is returned as the response which is used to pause/resume/stop this task.  
   
   Note: A `test.csv` file is present in root that can be used for this.
   
   
  2. **API to pause upload**
   
   `/data/pauseupload/`  
   Method: POST  
   The unique task Id is sent to the server to pause the upload.
   Respone - Status  
   
 
  3. **API to resume upload**
   
   `/data/resumeupload/`  
   Method: POST  
   The unique task Id is sent to the server to resume the upload.
   Respone - Status 
   
  4. **API to export data**
   
   `/data/dataexport/`  
   Method: GET  
   Get request is sent to the server then export data which is in a table is exported to a file which is saved in exports folder.
   The unique Task ID is returned as the response which is used to pause/resume/stop the task. 
   
   
   
  5. **API to pause export**
   
   `/data/pauseexport/`  
   Method: POST  
   The unique task Id is sent to the server to pause the export.
   Respone - Status    
   
 
  6. **API to resume export**
   
   `/data/resumeexport/`  
   Method: POST  
   The unique task Id is sent to the server to resume the export.
   Respone - Status    
   
  7. **API to Upload team CSV file**
   
   `/data/uploadteams/`  
   Method: POST  
   Server receives file with key as `file`  
   The unique Task ID is returned as the response which is used to pause/resume/stop this task.  
   
   Note: A `test.csv` file is present in root that can be used for this.
   
   
  8. **API to pause team csv upload**
   
   `/data/pauseuploadteam/`  
   Method: POST  
   The unique task Id is sent to the server to pause the upload.
   Respone - Status
   
  9. **API to resume team csv upload**
   
   `/data/pauseuploadteam/`  
   Method: POST  
   The unique task Id is sent to the server to resume the upload.
   Respone - Status 
   
 
  10. **API to terminate a task**
   
   `/data/terminate/`  
   Method: POST  
   The unique task Id is sent to the server to terminate any task.
   Respone - Status  
  
 
