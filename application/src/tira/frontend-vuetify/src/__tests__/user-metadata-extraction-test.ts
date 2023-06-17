import { extractRole } from '../utils'


function doc(html: string) {
    return new DOMParser().parseFromString(html, 'text/html')
}

test('Guest is the default role if a non-existing role is specified.', () => {
    let d = doc('<script id="user_metadata">{"role": "sda"}</script>')
    
    expect(extractRole(d)).toBe('guest')
});

test('Guest is the default role if the json can not be parsed.', () => {
    let d = doc('<script id="user_metadata">{"role": "}</script>')
    
    expect(extractRole(d)).toBe('guest')
});

test('Guest is the default role if a valid json is in a different tag.', () => {
    let d = doc('<script id="user_metadataXYZ">{"role": "admin"}</script>')
    
    expect(extractRole(d)).toBe('guest')
});

test('Extract admin if admin is specified.', () => {
    let d = doc('<script id="user_metadata">{"role": "admin"}</script>')
    
    expect(extractRole(d)).toBe('admin')
});

test('Extract participant if participant is specified.', () => {
    let d = doc('<script id="user_metadata">{"role": "participant"}</script>')
    
    expect(extractRole(d)).toBe('participant')
});

