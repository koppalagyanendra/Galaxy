document.querySelectorAll('.star, .planet').forEach(element => {
    element.addEventListener('click', async (e) => {
        const type = e.target.classList.contains('star') ? 'star' : 'planet';
        const id = e.target.dataset.id;

        const response = await fetch(`/details/${type}/${id}`);
        const data = await response.json();

        const modal = document.getElementById('details-modal');
        modal.innerHTML = `
            <h3>${data.name}</h3>
            <p>Size: ${data.size}</p>
            <p>Distance: ${data.distance}</p>
            <p>Description: ${data.description}</p>
            <button onclick="this.parentElement.style.display='none'">Close</button>
        `;
        modal.style.display = 'block';
        modal.classList.add('show');
    });
});

function adjustScaling() {
    const galaxy = document.querySelector('.galaxy-view');
    const aspectRatio = window.innerWidth / window.innerHeight;
    galaxy.style.transform = aspectRatio > 1.6 ? 'scale(0.8)' : 'scale(1)';
}

window.addEventListener('resize', adjustScaling);
adjustScaling();