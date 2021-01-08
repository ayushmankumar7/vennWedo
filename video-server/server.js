const express = require("express");
const app = express();
const fs = require("fs");
const mongodb = require('mongodb');
const url = 'mongodb://127.0.0.1/';


app.get("/", function (req, res) {
  res.sendFile(__dirname + "/index.html");
});


app.get('/load-video', function (req, res) {
  mongodb.MongoClient.connect(url, function (error, client) {
    if (error) {
      res.json(error);
      return;
    }
    const db = client.db('videos');
    const bucket = new mongodb.GridFSBucket(db);
    const videoUploadStream = bucket.openUploadStream('sample');
    const videoReadStream = fs.createReadStream('./sample.mp4');
    videoReadStream.pipe(videoUploadStream);
    res.status(200).send("Done...");
    // res.status(301).redirect('http://localhost:8000/')
  });
});

app.get("/play-video", function (req, res) {
  mongodb.MongoClient.connect(url, function (error, client) {
    if (error) {
      res.status(500).json(error);
      return;
    }

    const range = req.headers.range;
    if (!range) {
      res.status(400).send("Requires Range header");
    }

    const db = client.db('videos');
    
    db.collection('fs.files').findOne({}, (err, video) => {
      if (!video) {
        res.status(404).send("No video uploaded!");
        return;
      }

      const CHUNK_SIZE = 10**6;
      const videoSize = video.length;
      const start = Number(range.replace(/\D/g, ""));
      const end = Math.min(start+ CHUNK_SIZE, videoSize - 1);

      const contentLength = end - start + 1;
      const headers = {
        "Content-Range": `bytes ${start}-${end}/${videoSize}`,
        "Accept-Ranges": "bytes",
        "Content-Length": contentLength,
        "Content-Type": "video/mp4",
      };

      
      res.writeHead(206, headers);

      const bucket = new mongodb.GridFSBucket(db);
      const downloadStream = bucket.openDownloadStreamByName('sample', {
        start
      });

      
      downloadStream.pipe(res);
    });
  });
});

app.listen(8000, function () {
  console.log("Listening on port 8000!");
});




