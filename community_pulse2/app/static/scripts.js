document.getElementById('question-form').addEventListener('submit', async (event) => {
    event.preventDefault();
    const title = document.getElementById('title').value;
    const description = document.getElementById('description').value;

    const response = await fetch('/questions', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ title, description })
    });

    if (response.ok) {
        loadQuestions();
    }
});

async function loadQuestions() {
    const response = await fetch('/questions');
    const questions = await response.json();
    const list = document.getElementById('questions-list');
    list.innerHTML = '';
    questions.forEach(q => {
        const div = document.createElement('div');
        div.textContent = `Title: ${q.title} - Description: ${q.description}`;
        list.appendChild(div);
    });
}

loadQuestions();
