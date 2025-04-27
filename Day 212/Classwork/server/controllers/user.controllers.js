const users = []

const userRegister = (req, res) => {
    try {
        const {email, password} = req.body;

        const user = {
            email, password,
            profileImg: req.file.path
        }

        users.push(user);

    } catch (e) {
        res.status(500).json({message: e})
    }
};

module.exports = {userRegister};