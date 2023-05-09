import { ref } from 'vue'

export function extractTaskFromCurrentUrl() {
    let loc = ref(window.location).value.href
    
    if (loc.includes('task-overview/')) {
        return loc.split('task-overview/')[1].split('/')[0]
    }

    return null;
}

async function submitPost(url: string, params: [string: any]) {
    const csrf = ''
    const headers = new Headers({
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'X-CSRFToken': csrf
    })
    console.log(JSON.stringify(params))
    const response = await fetch(url, {
        method: "POST",
        headers,
        body: JSON.stringify(params)
    })
    if (!response.ok) {
        throw new Error(`Error fetching endpoint: ${url} with ${response.status}`);
    }
    let results = await response.json()
    if (results.status === 1) {
        throw new Error(`${results.message}`);
    }
    return results
}

async function get(url: string) {
    const response = await fetch(url)
    if (!response.ok) {
      throw new Error(`Error fetching endpoint: ${url} with ${response.status}`);
    }
    let results = await response.json()
    if (results.status === 1) {
      throw new Error(`${results.message}`);
    }
    return results
}