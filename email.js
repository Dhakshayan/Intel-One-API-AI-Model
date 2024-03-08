const nodemailer = require("nodemailer");

const transporter = nodemailer.createTransport({
  host: "smtp.ethereal.email",
  port: 587,
  secure: false, 
  auth: {
    user: "brice.conn@ethereal.email",
    pass: "sYDcGukDTVEaFwYCTS",
  },
});


async function main() {

  const info = await transporter.sendMail({
    from: '"SubZero Team" <subzero69@gmail.com>',
    to: "exmple@gmail.com, baz@example.com",
    subject: "Suggestions",
    text: "Placeholder Text", 
    html: "<h1>Placeholder Text</h1><br><b>Placeholder Text</b>",
  });

  console.log("Message sent: %s", info.messageId);
}

main().catch(console.error);
