// puppeteer-extra is a drop-in replacement for puppeteer,
// it augments the installed puppeteer with plugin functionality

const puppeteer = require("puppeteer");
const fs = require("fs");
const path = require("path");

// add stealth plugin and use defaults (all evasion techniques)
// const StealthPlugin = require("puppeteer-extra-plugin-stealth");

// puppeteer.use(StealthPlugin());

let browser;

let dirpath = path.join(__dirname, "../", "images");
console.log(dirpath);
// const dir = "../images";

if (!fs.existsSync(dirpath)) {
  fs.mkdirSync(dirpath);
}

const getScreenshot = async (url) => {
  try {
    browser = await puppeteer.launch({
      headless: true,
      // args: ["--no-sandbox", "--disable-setuid-sandbox"],
    });
    const page = await browser.newPage();

    await page.setViewport({
      height: 1920,
      width: 1080,
    });

    await page.goto(url, {
      waitUntil: "networkidle2",
    });

    let domain = String(url).split("/")[2];

    let imagename = `${domain}_${Math.floor(
      100000 + Math.random() * 900000
    )}.png`;

    await page.screenshot({
      path: `${dirpath}\\${imagename}`,
    });

    console.log("done - " + imagename);

    await browser.close();
    return imagename;
  } catch (error) {
    await browser.close();
    console.log(error);
  }
};

module.exports = { getScreenshot };
