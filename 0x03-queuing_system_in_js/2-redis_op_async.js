/**
 * connection to the
 * redis server
 */

import { createClient, print } from 'redis';
import { promisify } from 'util';
// eslint-disable-next-line no-unused-vars

// creating a client createClient
const client = createClient();
client.on('connect', () => console.log('Redis client connected to the server'))
  .on('error', (ERROR_MESSAGE) => console.log(`Redis client not connected to the server: ${ERROR_MESSAGE}`));

function setNewSchool(schoolName, value) {
  // seting the object
  client.set(schoolName, value, print);
}
const clientPromised = promisify(client.get).bind(client);
async function displaySchoolValue(schoolName) {
  clientPromised(schoolName)
    .then((res) => {
      console.log(res);
    })
    .catch((err) => {
      console.log(err);
    });
  // await client.get(schoolName, (err, result) => {
  //   if (err) {
  //     console.log(err);
  //     return;
  //   }
  //   console.log(result);
  // });
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
