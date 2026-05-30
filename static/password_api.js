                // password_api.js
async function requestPassword(length) {
    const response = await fetch('https://password-generator-kgvg.onrender.com/generate', {
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
    const response = await fetch('https://password-generator-kgvg.onrender.com/check', {
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
