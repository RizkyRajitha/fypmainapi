const express = require("express");
// const bodyParser = require('body-parser');
// const cors = require('cors');
const { Client } = require("pg");

const client = new Client({
  connectionString:
    "postgres://hsahkdaw:JWgvRmKRS-qp_7KERaEHF03KZs2b6Lj5@lallah.db.elephantsql.com:5432/hsahkdaw",
});

const port = process.env.PORT || 6000;

const app = express();
app.use(express.json());
app.use(express.urlencoded({ extended: true }));
// app.use(bodyParser.json())
// var corsOptions = {
//   credentials: true, origin: true
// }
// app.use(cors(corsOptions))

//check URL in database API
app.post("/api/searchUrl", async (req, res) => {
  let domainName;
  if (req.body.url.split("//")[1]) {
    domainName = req.body.url.split("//")[1].split("/")[0];
  } else {
    domainName = req.body.url.split("/")[0];
  }
  console.log(domainName);
  try {
    let wl = await client.query("SELECT * from alexa WHERE url = $1", [
      domainName,
    ]);

    if (wl.rowCount) {
      res.json({
        whiteList: true,
        blackList: false,
        notFound: false,
      });
      return;
    }

    let bl = await client.query("SELECT * FROM phishtank WHERE url LIKE $1", [
      req.body.url,
    ]);

    let found = bl.rowCount ? true : false;
    res.json({
      whiteList: false,
      blackList: found,
      notFound: !found,
    });
  } catch (error) {
    res.status(500).json({ message: error.message });
  }
});

app.get("/aa", async (req, res) => {
  let bl = await client.query("SELECT * FROM phishtank LIMIT 100");
  console.log(bl.rows);
  res.json(bl.rows);
});

client.connect((err) => {
  if (err) {
    console.error("connection error", err.stack);
  } else {
    console.log("connected postgreSQL");
  }
});

app.listen(port, () => {
  console.log("server is running on port: " + port);
});

// .then((presult) => {
//   let found = presult.rowCount ? true : false;
//   res.json({
//     whiteList: false,
//     blackList: found,
//     notFound: !found,
//   });
// })
// .catch((err) => {
//   console.log(err);
// });

// .then((result) => {
//   let found = result.rowCount ? true : false;

//   if (found) {
//     res.json({
//       whiteList: true,
//       blackList: false,
//       notFound: false,
//     });
//   }

// //check the URL in white list
// client
//   .query("SELECT * from alexa WHERE url = $1", [domainName])
//   .then((result) => {
//     let found = result.rowCount ? true : false;

//     if (found) {
//       res.json({
//         whiteList: true,
//         blackList: false,
//         notFound: false,
//       });
//     }
//     else {
//       //check the URL in black list
//       client
//         .query("SELECT * FROM phishtank WHERE url LIKE $1", [req.body.url])
//         .then((presult) => {
//           let found = presult.rowCount ? true : false;
//           res.json({
//             whiteList: false,
//             blackList: found,
//             notFound: !found,
//           });
//         })
//         .catch((err) => {
//           console.log(err);
//         });
//     }
//   })
//   .catch((err) => {
//     console.log(err);
//   });
