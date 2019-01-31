Backend Test Automation
---

> We are a python shop, but use whatever you know best.

### This is our imaginary system:


```            
+------+  +------+
|Worker|  |Worker|
+-----++  +---+--+
      |       |
      |       |              +----------+
   +--v-------v---+          |          |
   | Indexing API |          |   User   +-+
   +------+-------+          |          | |
          |                  +----------+ |
          |                               |
  +-------v-------+                       |
  |               |     +-------------+   |
  | ElasticSearch <-----+  Query API  <---+
  |               |     +-------------+
  +---------------+
```



- Workers insert new data to ElasticSearch through the `Indexing API`.
- The number of workers can change
- User runs queries against ElasticSearch through the `Query API`.

---

### 1. Run the example API Server

- Start API server on http://127.0.0.1:1234
    ```bash
    docker run -it -e WORKERS=2 --rm -p 1234:1234 drorwolmer/stress_test   
    ```
- You can change the amount of workers used by API server by changing the `WORKERS` environment variable.
- API documentation is available on http://127.0.0.1:1234/swagger-ui/

### 2. Write a simulator to stress test the `Indexing API` ** WITH RANDOM DATA **

```json
POST /api/index
{
    "name": "My_document_2018.pdf",
    "directory": "/home/Dror/Documents/Legal/",
    "host": "FileServer1",
    "file_size": 19222,
    "permissions": {
      "dror": "READ",
      "itai": "READ_WRITE"
    }
}
```

- In our system, we want to be able to index 200 of documents per-second.
- Each document **has to be unique** (different filesize, name, etc.)
- Data from the simulator needs to resemble real-world data distribution.
  - For example, there is a limited number of `hosts`, `directories`
  - There is a finite number of file extensions
- `Indexing API` can handle multiple connections
- Understand the maximum requests per-second it can handle.


  
### 3. Monitor how the `query` API performs under stress
- We want to understand how the dashboard query performs both under stress and while idle
  . Interesting metrics are timeouts, latency, tail latency, etc.

```json
GET /api/query/dashboard
```

---
