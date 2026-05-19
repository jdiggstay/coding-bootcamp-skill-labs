const express = require("express");
const app = express();

const PORT = 3000;

app.get("/", (req, res) => {
    res.send("Healthcare Analytics API");
})

app.get("/patients", (req, res) => {
    res.json([
        { id: 1, name: "Anna", bmi: 23.4 },
        { id: 2, name: "Benjamin", bmi: 32.1 },
        { id: 3, name: "Carol", bmi: 21.2}
    ]);
});

app.listen(PORT, () => {
    console.log('Server running at http://localhost:${PORT}');
});