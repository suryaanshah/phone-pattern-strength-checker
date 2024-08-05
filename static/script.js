// script.js
const container = document.querySelector('.pattern-container');

function createDots() {
  for (let i = 0; i < 9; i++) {
    const dot = document.createElement('div');
    dot.classList.add('dot');
    container.appendChild(dot);
  }
}

createDots();
