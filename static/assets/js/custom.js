console.log("hell");

const email = document.getElementById("InputEmail");
const password = document.getElementById("InputPassword");
const loginForm = document.getElementById("loginForm");
const cardAccount = document.querySelector(".card-account");
const imgProfile = document.getElementById("img-profile");

imgProfile.addEventListener("click", () => {
  cardAccount.classList.toggle("card-account");
  cardAccount.classList.toggle("display-opt");
});

console.log(loginForm);
