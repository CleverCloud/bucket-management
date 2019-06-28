Bucket Management
----
Helper tools to manipulate S3 like storage

Quick Start
---
```
From bucket_management import ClBucketManagement

manager = ClBucketManagement(api_key,
                             secret_key,
                             host)
                             
```

* `api_key`: Key to connect to your targeted S3 like
* `secret_key`: Secret Key to connect to your targeted S3 like 
* `host` : Host of your targeted S3

Methods
---
Available methods are :

* save_big_files:
  
   Send big file to a specific bucket
   
   **Params:**
   * bucket_name : name of the targeted bucket
   * key_id : key id of your file
   * source_file_path : file path of the source file (absolute or relative)
   * chunk_sze (optional): chunk size send to the bucket. *default:* 52428800

* save_file:

   Send file to a specific bucket. Key id in the bucket is the filename.
   
   **Params:**
   * bucket_name : name of the targeted bucket
   * source_file_path : file path of the source file (absolute or relative)

* get_data:

  Get data from a specific bucket based on its key id
  
  **Params:**
  * bucket_name : name of the targeted bucket
  * key_id: wanted data key id
  * dest_fld (optional): destination folder to download the data (absolute or relative). *default:* current directory

* get_all_key:

   get all existing key id in a bucket
   
  **Params:**
   * bucket_name : Name of the targeted bucket

   **Returns:**
   List of existing key id
 
* get_all_from_bucket:

   get all the existing data from a bucket

   **Params:**
   * bucket_name : Bucket source
   * dest_fld (optional): destination folder to download the data (absolute or relative). *default:* current directory

* get_all_bucket:

   get all existing bucket names

   **Params:**
   
   NO PARAMETERS NEEDED

   **Returns:**
   List of existing bucket name

* create_bucket:

   Create a new bucket
   
   **Params:**
   * bucket_name: Bucket name. Must bu unique.

   **Returns:**
   New created bucket object

* delete_keys:

  Delete specific data in a bucket based on its key id
  
  **Params:**
  * bucket_name : Bucket which contain the data
  * keys : Key id of the data to delete

* delete_bucket:

    Delete a bucket
    
    **Params**
    * bucket_name: Bucket name of the targeted bucket
    * allow_full_bucket_deletion (optional): If `true` delete a bucket and its content. Else only empty bucket can be deleted.
    *default:* `False`
