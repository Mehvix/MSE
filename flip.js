let n = true;
function flippy() {
    n = !n;
    let fn = "";
    if (n) {
        fn = "py-qr-reg.png";
    } else {
        fn = "py-qr-min.png";
    }
    document.getElementById("QR").setAttribute("src", fn);
}
