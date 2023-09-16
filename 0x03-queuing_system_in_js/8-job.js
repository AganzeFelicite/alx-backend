/**
 * this is a new job
 * added to the job queue
 */
// const kue = require('kue')

// .const queue = kue.createQueue()

export default function createPushNotificationsJobs(jobs, queue) {
  if (!Array.isArray(jobs)) return new Error('Jobs is not an array');
  jobs.forEach((item, _) => {
    const job = queue.create('push_notification_code_3', item);
        job.save((err) => {
          if (!err) {
          console.log(`Notification job created: ${job.id}`);
        }
      })
      job.on('complete', () => console.log(`Notification job ${job.id} completed`))
      job.on('failed', (err) => {
        if (err) {
          console.log(`Notification job ${job.id} failed: ${err}`);
        }
      })
      job.on('progress', (e) => console.log(`Notification job ${job.id} ${e}% complete`));
  });
}

// module.exports = createPushNotificationsJobs;
