/**
 * connection to the
 * redis server
 */

import { createClient } from 'redis';
// eslint-disable-next-line no-unused-vars
export default function redisClient() {
  // creating a client createClient
  const client = createClient();
  client.on('connect', () => {
    console.log('Redis client connected to the server');
  })
    .on('error', (ERROR_MESSAGE) => {
      console.log(`Redis client not connected to the server: ${ERROR_MESSAGE}`);
    });
}
redisClient();
