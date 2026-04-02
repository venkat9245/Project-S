// Glow animation
setInterval(() => {
  const title = document.querySelector("h1");
  title.style.textShadow =
    "0 0 " + (10 + Math.random() * 20) + "px #22c55e";
}, 800);

// Threat color logic
window.onload = () => {
  const bar = document.getElementById("progressBar");

  if (bar) {
    const width = parseInt(bar.style.width);

    if (width <= 30) {
      bar.style.background = "linear-gradient(90deg, #22c55e, #4ade80)";
    } 
    else if (width <= 70) {
      bar.style.background = "linear-gradient(90deg, #facc15, #fde047)";
    } 
    else {
      bar.style.background = "linear-gradient(90deg, #ef4444, #f87171)";
    }
  }
};
