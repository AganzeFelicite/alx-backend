/**
 * a publisher creation
 */

import { createClient } from 'redis';

const publisher = createClient();
publisher.on('connect', () => console.log('Redis client connected to the server'))
  .on('error', (ERROR_MESSAGE) => console.log(`Redis client not connected to the server: ${ERROR_MESSAGE}`));

function publishMessage(message, time) {
  console.log('About to send MESSAGE');
  setTimeout(() => {
    publisher.publish('holberton school channel', message);
  }, time);
}
publishMessage('Holberton Student #1 starts course', 100);
publishMessage('Holberton Student #2 starts course', 200);
publishMessage('KILL_SERVER', 300);
publishMessage('Holberton Student #3 starts course', 400);
