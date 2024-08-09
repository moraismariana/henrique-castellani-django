//PORTFOLIO
const botao = document.querySelector(".button");

function verMais() {
  const elementos = document.querySelectorAll(".clientes-item-extra");
  elementos.forEach((elemento) => {
    elemento.classList.toggle("none");
  });

  // Verificar se os elementos estão visíveis ou não e atualizar o texto do botão
  const algumElementoVisivel = Array.from(elementos).some(
    (elemento) => !elemento.classList.contains("none")
  );

  if (algumElementoVisivel) {
    botao.textContent = "ver menos";
  } else {
    botao.textContent = "ver mais";
  }
}

botao.addEventListener("click", verMais);

// MENU MOBILE
function menuShow() {
  let menuMobile = document.querySelector(".mobile-menu");
  let background = document.querySelector(
    ".mobile-menu-bg .background-overlay"
  );
  menuMobile.classList.toggle("none");
  background.classList.toggle("none");
}

document.querySelectorAll(".mobile-menu a").forEach((link) => {
  link.addEventListener("click", function () {
    menuShow();
  });
});
