document.querySelectorAll("button").forEach((item) => {
  item.addEventListener("click", () => {
    console.log(item);
    item.nextElementSibling.classList.toggle("newlist");
  });
});
