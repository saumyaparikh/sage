const express = require("express");
const app = express();

app.set(express.static(path.join(__dirname, "public")));

app.set("view engine", "ejs");
app.set("views", path.join(__dirname, "/views"));

app.get("/", (req, res) => {
  res.send("Hi");
});
app.listen(3000, () => {
  console.log("Listening on port 3000");
});
