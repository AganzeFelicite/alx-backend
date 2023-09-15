/**
 * connection to the
 * redis server
 */

import { createClient, print } from 'redis';
// import { promisify } from 'util';
// eslint-disable-next-line no-unused-vars

// creating a client createClient
const client = createClient();
client.on('connect', () => console.log('Redis client connected to the server'))
  .on('error', (ERROR_MESSAGE) => console.log(`Redis client not connected to the server: ${ERROR_MESSAGE}`));

// function setNewSchool(schoolName, value) {
//   // seting the object
//   client.set(schoolName, value, print);
// }

client.hset('HolbertonSchools', 'Portland', 50, print);
client.hset('HolbertonSchools', 'Seattle', 80, print);
client.hset('HolbertonSchools', 'New York', 20, print);
client.hset('HolbertonSchools', 'Bogota', 20, print);
client.hset('HolbertonSchools', 'Cali', 40, print);
client.hset('HolbertonSchools', 'Paris', 2, print);

// displaying store htbale store in redis

client.hgetall('HolbertonSchools', (err, result) => {
  if (err) {
    console.log(err);
    throw err;
  } else {
    console.log(result);
  }
});
