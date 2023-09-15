/**
 * a subscriber creation
 */

import { createClient } from 'redis';

const subscriber = createClient();
subscriber.on('connect', () => console.log('Redis client connected to the server'))
  .on('error', (ERROR_MESSAGE) => console.log(`Redis client not connected to the server: ${ERROR_MESSAGE}`));
subscriber.subscribe('holberton school channel');
subscriber.on('message', (channel, message) => {
  console.log(message);
  if (message === 'KILL_SERVER') {
    subscriber.unsubscribe(channel);
    subscriber.end(true);
  }
});
