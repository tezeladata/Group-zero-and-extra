const multer = require("multer");

const storage = multer.diskStorage({
    filename: function (req, file, cb) {
        cb(null, Date.now() + file.originalname);
    },
    destination: function (req, file, cb) {
        cb(null, "images/")
    }
})

const upload = multer({storage});

module.exports = upload;