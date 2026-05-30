                // password_api.js
async function requestPassword(length) {
    const response = await fetch('http://127.0.0.1:5000/generate', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ length })
    });
    if (!response.ok) {
        throw new Error('Failed to generate password');
    }
    const data = await response.json();
    return data.password;
}

async function checkPassword(password) {
    const response = await fetch('http://127.0.0.1:5000/check', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ password })
    });
    if (!response.ok) {
        throw new Error('Failed to check password');
    }
    const data = await response.json();
    return data;
}
