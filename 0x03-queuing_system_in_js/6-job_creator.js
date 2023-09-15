/** *
 * creating job queues using kue
 */

const kue = require('kue');

const queue = kue.createQueue();
const jobObj = {
  phoneNumber: '0787692740',
  message: 'transaction completed',
};
const job = queue.create('push_notification_code', jobObj);
job.save((err) => {
  if (!err) {
    console.log(`Notification job created: ${job.id}`);
  }
});
job.on('complete', () => {
  console.log('Notification job completed');
});
job.on('failed', () => console.log('Notification job failed'));
