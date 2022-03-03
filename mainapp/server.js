const express = require("express");
const {
  getUrlAnalyzerOutput,
  getFaviconAnalyzerOutput,
  getImageAnalyzerOutput,
  getBlackListWhiteListOutput,
} = require("./lib/service");

const port = 4000;
const app = express();

app.use(express.json());
app.use(express.urlencoded({ extended: true }));

app.get("/", (req, res) => {
  res.json({ hello: "world" });
});

app.post("/analyze", async (req, res) => {
  console.log(req.body);

  if (!req.body.url) {
    res.status(400).json({ message: "no url found" });
    return;
  }

  try {
    let proarr = [
      getFaviconAnalyzerOutput(req.body.url),
      getUrlAnalyzerOutput(req.body.url),
      // getImageAnalyzerOutput(req.body.url),
      getBlackListWhiteListOutput(req.body.url),
    ];

    let [predFavicon, predUrl, blwlout] = await Promise.all(proarr);

    if (blwlout.blackList) {
      res.json({ result: true });
      return;
    }
    if (blwlout.whiteList) {
      res.json({ result: false });
      return;
    }

    console.log(predUrl);
    console.log(predFavicon);
    console.log(blwlout);

    res.json({ result: predUrl.result });
  } catch (error) {
    console.log(error);
    res.status(500).json({ message: error.message });
  }
});

app.listen(port, () => {
  console.log("Express server listning on port " + port);
});
