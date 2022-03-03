const fetch = require("node-fetch");
const FormData = require("form-data");
const fs = require("fs");
const path = require("path");

const { getScreenshot } = require("./puppet");

const urlAnalyzerEndpoint = "http://127.0.0.1:5000/predict";
const faviconAnalyzerEndpoint = "http://127.0.0.1:8000/query";
const blackListWhiteListEndpoint = "http://127.0.0.1:6000/api/searchUrl";

const getUrlAnalyzerOutput = async (url) => {
  let res = await fetch(urlAnalyzerEndpoint, {
    headers: {
      "Content-Type": "application/json",
    },
    method: "POST",
    body: JSON.stringify({ url }),
  });

  if (!res.ok) {
    const error = new Error("An error occurred while posting the data");
    throw error;
  }

  return await res.json();
};

const getFaviconAnalyzerOutput = async (url) => {
  let res = await fetch(faviconAnalyzerEndpoint, {
    headers: {
      "Content-Type": "application/json",
    },
    method: "POST",
    body: JSON.stringify({ url }),
  });

  if (!res.ok) {
    const error = new Error("An error occurred while posting the data");
    throw error;
  }

  return await res.json();
};

const getImageAnalyzerOutput = async (url) => {
  let imgName = await getScreenshot(url);

  let dirpath = path.join(__dirname, "../", "images");
  let imgpath = `${dirpath}\\${imgName}`;

  console.log(imgpath);

  let readStream = fs.createReadStream(imgpath);
  let form = new FormData();
  form.append("photo", readStream);

  //   let res = await fetch(faviconAnalyzerEndpoint, {
  //     headers: {
  //       "Content-Type": "application/json",
  //     },
  //     method: "POST",
  //     body: form,
  //   });

  //   if (!res.ok) {
  //     const error = new Error("An error occurred while posting the data");
  //     throw error;
  //   }

  //   return await res.json();
  //   fs.unlinkSync(imgpath);
};

const getBlackListWhiteListOutput = async (url) => {
  let res = await fetch(blackListWhiteListEndpoint, {
    headers: {
      "Content-Type": "application/json",
    },
    method: "POST",
    body: JSON.stringify({ url }),
  });

  if (!res.ok) {
    const error = new Error("An error occurred while posting the data");
    throw error;
  }

  return await res.json();
};

module.exports = {
  getUrlAnalyzerOutput,
  getFaviconAnalyzerOutput,
  getImageAnalyzerOutput,
  getBlackListWhiteListOutput,
};
