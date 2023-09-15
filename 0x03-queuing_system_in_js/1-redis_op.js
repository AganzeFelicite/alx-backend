/**
 * connection to the
 * redis server
 */

import { createClient, print } from 'redis';
// eslint-disable-next-line no-unused-vars

// creating a client createClient
const client = createClient();
client.on('connect', () => console.log('Redis client connected to the server'))
  .on('error', (ERROR_MESSAGE) => console.log(`Redis client not connected to the server: ${ERROR_MESSAGE}`));

function setNewSchool(schoolName, value) {
  // seting the object
  client.set(schoolName, value, print);
}

function displaySchoolValue(schoolName) {
  client.get(schoolName, (err, result) => {
    if (err) {
      console.log(err);
      return;
    }
    console.log(result);
  });
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
