import { ref } from 'vue'

export function extractTaskFromCurrentUrl() {
    let loc = ref(window.location).value.href
    
    if (loc.includes('task-overview/')) {
        return loc.split('task-overview/')[1].split('/')[0]
    }

    return null;
}

export function extractDatasetFromCurrentUrl(options: Array<any> = [], default_choice: string='') {
    var loc = ref(window.location).value.href
    var dataset_from_url = ''
    let to_split = 'task-overview/' + extractTaskFromCurrentUrl() + '/'
    
    if (loc.includes(to_split)) {
        dataset_from_url = loc.split(to_split)[1].split('/')[0]
    }

    if (options.length === 0) {
        return dataset_from_url
    }

    if (default_choice !== '') {
        for (var dataset of options) {
            if (default_choice === dataset['dataset_id']) {
                return dataset['dataset_id']
            }
        }
    }

    var ret = ''

    for (var dataset of options) {
        if ((dataset_from_url !== '' && dataset_from_url === dataset['dataset_id']) || ret === '') {
            ret = dataset['dataset_id']
        }
    }

    return ret
}

export function chanceCurrentUrlToDataset(dataset: string) {
    var loc = ref(window.location).value.href

    if (loc.includes('task-overview/')) {
        loc = loc.split('task-overview/')[0] + 'task-overview/' + loc.split('task-overview/')[1].split('/')[0] + '/' + dataset
        history.replaceState({'url': loc}, 'TIRA', loc)
    }
}

export function extractRole() {
    return 'guest'
}

export function reportError(error: any) {
    console.log(error)
}

export function inject_response(obj: any, default_values: any={}, debug=false) {
    let object_to_inject_data = obj.$data
    return function(message: any) {
      let available_keys = new Set<string>(Object.keys(message['context']))

      for (var key of Object.keys(object_to_inject_data)) {
        if (available_keys.has(key)) {
          object_to_inject_data[key] = message['context'][key]
        }
      }

      for (var key of Object.keys(default_values)) {
        object_to_inject_data[key] = default_values[key]
      }

      if (debug) {
        console.log(object_to_inject_data)
      }
    }
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

export async function get(url: string) {
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