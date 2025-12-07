import clsx from 'clsx';
import Heading from '@theme/Heading';
import styles from './styles.module.css';

const FeatureList = [
  {
    title: 'The Nervous System (ROS 2)',
    description: (
      <>
        Master the middleware of robotics. Learn nodes, topics, and services 
        to bridge Python AI agents to real-world hardware controllers 
        using <code>rclpy</code> and URDF.
      </>
    ),
  },
  {
    title: 'The Digital Twin (Isaac Sim)',
    description: (
      <>
        Train before you deploy. Build photorealistic physics simulations 
        in NVIDIA Isaac Sim & Gazebo to test gravity, collisions, and 
        sensors without breaking hardware.
      </>
    ),
  },
  {
    title: 'The AI Brain (VLA)',
    description: (
      <>
        The convergence of LLMs and Robotics. Implement Vision-Language-Action 
        models to translate natural language commands into complex 
        humanoid movements.
      </>
    ),
  },
];

// Removed 'Svg' from props
function Feature({title, description}) {
  return (
    <div className={clsx('col col--4')}>
      {/* Removed the div containing the Svg tag */}
      <div className="text--center padding-horiz--md">
        <Heading as="h3">{title}</Heading>
        <p>{description}</p>
      </div>
    </div>
  );
}

export default function HomepageFeatures() {
  return (
    <section className={styles.features}>
      <div className="container">
        <div className="row">
          {FeatureList.map((props, idx) => (
            <Feature key={idx} {...props} />
          ))}
        </div>
      </div>
    </section>
  );
}