/**
 * this is job queue
 * procesor
 */

const kue = require('kue');

const queue = kue.createQueue();
function notifications(phoneNumber, message, done) {
  console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);
  done();
}

queue.process('push_notification_code', (job, done) => {
  notifications(job.data.phoneNumber, job.data.message, done);
});
