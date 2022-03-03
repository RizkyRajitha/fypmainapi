// // puppeteer-extra is a drop-in replacement for puppeteer,
// // it augments the installed puppeteer with plugin functionality

// const puppeteer = require("puppeteer");
// // const fetch = require("node-fetch");
// const fs = require("fs");

// // add stealth plugin and use defaults (all evasion techniques)
// // const StealthPlugin = require("puppeteer-extra-plugin-stealth");

// // puppeteer.use(StealthPlugin());

// let browser;

// const dir = "./images";

// const run = async () => {
//   if (!fs.existsSync(dir)) {
//     fs.mkdirSync(dir);
//   }

//   urlarr = [
//     "https://online.boc.lk/T001/channel.jsp",
//     "https://internetbank.nsb.lk/#%20",
//   ];

//   browser = await puppeteer.launch({
//     headless: false,
//     // args: ["--no-sandbox", "--disable-setuid-sandbox"],
//   });
//   let promisearr = [];

//   urlarr.forEach(async (element) => {
//     let domain = String(element).split("/")[2];
//     console.log(domain);
//     promisearr.push(getscreenshot(element, domain, 1920, 1080));
//     promisearr.push(getscreenshot(element, domain, 414, 896));
//   });

//   try {
//     await Promise.all(promisearr);
//     await browser.close();
//   } catch (error) {
//     console.log(error);
//   }

//   // await browser.close();
// };

// run();

// async function getscreenshot(url, domain, width, height) {
//   const page = await browser.newPage();

//   await page.setViewport({
//     width,
//     height,
//   });

//   await page.goto(url, {
//     waitUntil: "networkidle2",
//   });

//   await page.screenshot({
//     path: `./images/${domain}-${width}X${height}-login.png`,
//   });

//   console.log("done - " + domain);
//   // await browser.close();
// }
