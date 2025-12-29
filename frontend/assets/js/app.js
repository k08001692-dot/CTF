function addToCart() {
  const qty = document.getElementById("quantity").value;
  const coupon = document.getElementById("coupon").value;

  document.getElementById("message").innerText =
    "Book added to cart successfully!";
}
