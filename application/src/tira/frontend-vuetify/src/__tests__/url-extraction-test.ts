import { extractTaskFromCurrentUrl, extractDatasetFromCurrentUrl, extractCurrentStepFromCurrentUrl, extractSubmissionTypeFromCurrentUrl, extractUserFromCurrentUrl} from '../utils'

Object.defineProperty((window as Window), 'location', {
    value: {
      href: ''
    },
    writable: true // possibility to override
  });

test('Task from current Url should be Null.', () => {
    (window as Window).location.href = "http://dummy.com";
    expect(extractTaskFromCurrentUrl()).toBeNull();
});

test('Task from Url without Subpath Should be correct.', () => {
    (window as Window).location.href = 'task-overview/abc'
    expect(extractTaskFromCurrentUrl()).toStrictEqual('abc');
});

test('Task from Url without Subpath Should be correct with question mark.', () => {
  (window as Window).location.href = 'task-overview/abc?sada'
  expect(extractTaskFromCurrentUrl()).toStrictEqual('abc');
});

test('Task from Url without Subpath Should be correct with # symbol.', () => {
  (window as Window).location.href = 'task-overview/abc#sa'
  expect(extractTaskFromCurrentUrl()).toStrictEqual('abc');
});

test('Task from Url with Subpath Should be correct.', () => {
    (window as Window).location.href = 'task-overview/1234/'
    expect(extractTaskFromCurrentUrl()).toStrictEqual('1234');
});

test('Dataset from Url without dataset should be the empty string.', () => {
  (window as Window).location.href = 'task-overview/abc/'
  expect(extractDatasetFromCurrentUrl()).toStrictEqual('');
});

test('Dataset from current Url should be Null.', () => {
  (window as Window).location.href = "http://dummy.com";
  expect(extractDatasetFromCurrentUrl()).toStrictEqual('');
});

test('Dataset from Url without dataset should be the empty string even when not exists.', () => {
  (window as Window).location.href = 'task-overview/1234'
  expect(extractDatasetFromCurrentUrl()).toStrictEqual('');
});

test('Dataset from Url without Subpath Should be correct.', () => {
  (window as Window).location.href = 'task-overview/abc/ds'
  expect(extractDatasetFromCurrentUrl()).toStrictEqual('ds');
});

test('Dataset from Url without Subpath Should be correct with question mark.', () => {
  (window as Window).location.href = 'task-overview/abc/ds?xy=1'
  expect(extractDatasetFromCurrentUrl()).toStrictEqual('ds');
});

test('Dataset from Url without Subpath Should be correct with # symbol.', () => {
  (window as Window).location.href = 'task-overview/abc/ds#asdad'
  expect(extractDatasetFromCurrentUrl()).toStrictEqual('ds');
});

test('Dataset from Url with Subpath Should be correct.', () => {
  (window as Window).location.href = 'task-overview/1234/dataset-01/'
  expect(extractDatasetFromCurrentUrl()).toStrictEqual('dataset-01');
});

test('Dataset is extracted with precedence from the default_choice if available.', () => {
  (window as Window).location.href = 'task-overview/abc/ds'

  let options = [{'dataset_id': 'ds'}, {'dataset_id': 'something-is-selected'}, {'dataset_id': 'ds2'}]
  let selectedDataset = 'something-is-selected'

  expect(extractDatasetFromCurrentUrl(options, selectedDataset)).toStrictEqual('something-is-selected');
});

test('First Dataset is extracted if the default_choice is not available.', () => {
  (window as Window).location.href = 'task-overview/abc'

  let options = [{'dataset_id': 'ds'}, {'dataset_id': 'something-is-selected'}, {'dataset_id': 'ds2'}]
  let selectedDataset = 'does-not-exist'

  expect(extractDatasetFromCurrentUrl(options, selectedDataset)).toStrictEqual('ds');
});


test('Dataset from URL is extracted if default_choice is wrong.', () => {
  (window as Window).location.href = 'task-overview/abc/ds2'

  let options = [{'dataset_id': 'ds'}, {'dataset_id': 'something-is-selected'}, {'dataset_id': 'ds2'}]
  let selectedDataset = 'does-not-exist'

  expect(extractDatasetFromCurrentUrl(options, selectedDataset)).toStrictEqual('ds2');
});

test('Dataset from URL is extracted if no default_choice is available.', () => {
  (window as Window).location.href = 'task-overview/abc/ds2'

  let options = [{'dataset_id': 'ds'}, {'dataset_id': 'something-is-selected'}, {'dataset_id': 'ds2'}]
  let selectedDataset = ''

  expect(extractDatasetFromCurrentUrl(options, selectedDataset)).toStrictEqual('ds2');
});


test('First dataset is used if dataset from URL does not exist.', () => {
  (window as Window).location.href = 'task-overview/abc/ds2'

  let options = [{'dataset_id': 'ds'}, {'dataset_id': 'something-is-selected'}, {'dataset_id': 'ds22'}]
  let selectedDataset = ''

  expect(extractDatasetFromCurrentUrl(options, selectedDataset)).toStrictEqual('ds');
});


//TODO check if more tests are needed, especially regarding the optional url-parameters,
test('Task extracted from submission route should be correct, regardless of nesting-depth', () => {
  (window as Window).location.href = '/frontend-vuetify/submit/task-1234/user/user-test/chosen-submission-type/current-step'

  expect(extractTaskFromCurrentUrl()).toStrictEqual('task-1234');
});

test('User extracted from submission route should be correct', () => {
  (window as Window).location.href = '/frontend-vuetify/submit/task-1234/user/user-test/chosen-submission-type/current-step'

  expect(extractUserFromCurrentUrl()).toStrictEqual('user-test');
});
test('User extracted from submission route with subpath should be correct', () => {
  (window as Window).location.href = '/frontend-vuetify/submit/task-1234/user/user-test/'

  expect(extractUserFromCurrentUrl()).toStrictEqual('user-test');
});

//TODO test for guest user

test('Submission-type extracted from submission route should be correct', () => {
  (window as Window).location.href = '/frontend-vuetify/submit/task-1234/user/user-test/chosen-submission-type/current-step'

  expect(extractSubmissionTypeFromCurrentUrl()).toStrictEqual('chosen-submission-type');
});

test('Submission-type extracted from submission route without step should be correct', () => {
  (window as Window).location.href = '/frontend-vuetify/submit/task-1234/user/user-test/chosen-submission-type'

  expect(extractSubmissionTypeFromCurrentUrl()).toStrictEqual('chosen-submission-type');
});

test('Submission-type extracted from submission route without step, but subpath should be correct', () => {
  (window as Window).location.href = '/frontend-vuetify/submit/task-1234/user/user-test/chosen-submission-type/'

  expect(extractSubmissionTypeFromCurrentUrl()).toStrictEqual('chosen-submission-type');
});

test('Submission-type extracted from submission route should be null if not provided', () => {
  (window as Window).location.href = '/frontend-vuetify/submit/task-1234/user/user-test'

  expect(extractSubmissionTypeFromCurrentUrl()).toBeNull();
});

test('Submission-type extracted from submission route with subpath should be null', () => {
  (window as Window).location.href = '/frontend-vuetify/submit/task-1234/user/user-test/'

  expect(extractSubmissionTypeFromCurrentUrl()).toBeNull();
});
test('Current step extracted from submission route should be null if not provided', () => {
  (window as Window).location.href = '/frontend-vuetify/submit/task-1234/user/user-test/chosen-submission-type'

  expect(extractCurrentStepFromCurrentUrl()).toBeNull();
});

test('Current step extracted from submission route should be correct', () => {
  (window as Window).location.href = '/frontend-vuetify/submit/task-1234/user/user-test/chosen-submission-type/current-step'

  expect(extractCurrentStepFromCurrentUrl()).toStrictEqual('current-step');
});
test('Expect current step from subpath to be null if not exists', () => {
  (window as Window).location.href = '/frontend-vuetify/submit/task-1234/user/user-test/chosen-submission-type/'

  expect(extractCurrentStepFromCurrentUrl()).toBeNull();
});

test('First dataset is used if dataset from URL does not exist and default_choise is wrong.', () => {
  (window as Window).location.href = 'task-overview/abc/ds2'

  let options = [{'dataset_id': 'ds'}, {'dataset_id': 'something-is-selected'}, {'dataset_id': 'ds3'}]
  let selectedDataset = 'does-not-exist'

  expect(extractDatasetFromCurrentUrl(options, selectedDataset)).toStrictEqual('ds');
});
