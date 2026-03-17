const { check, validationResult } = require("express-validator");



// Registration validation rules
const registerValidation = [
  check("email")
    .notEmpty()
    .withMessage("Email is required")
    .isEmail()
    .withMessage("Invalid email format"),
  check("password")
    .isLength({ min: 8 })
    .withMessage("Password must be at least 8 characters"),
  check("name")
    .notEmpty()
    .withMessage("Name is required"),
];

// Custom validation middleware
function validateRequest(req, res, next) {
  const errors = validationResult(req);

  if (!errors.isEmpty()) {
    return res.status(400).json({
      error: "Validation failed",
      details: errors.array(),
    });
  }



  next();
}

module.exports = {
  registerValidation,
  validateRequest,

};
