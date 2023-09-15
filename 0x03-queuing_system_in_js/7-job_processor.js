/**
 * this is a file that creates a job processor
 * for the jobs in 7-job_creator
 */

const kue = require('kue');

const queue = kue.createQueue();

const arrayObBlackListNumbers = ['4153518780', '4153518781'];

function sendNotification(phoneNumber, message, job, done) {
  job.progress(0, 100);

  if (arrayObBlackListNumbers.includes(phoneNumber)) {
    console.log(`Phone number ${phoneNumber} is blacklisted`);
    done(Error(`Phone number ${phoneNumber} is blacklisted`));
  } else {
    job.progress(50, 100);
    console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);
    setTimeout(() => {
      done();
    }, 1000);
  }
}
queue.process('push_notification_code_2', (job, done) => {
  sendNotification(job.data.phoneNumber, job.data.message, job, done);
});
