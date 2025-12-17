import clsx from 'clsx';
import Link from '@docusaurus/Link';
import useDocusaurusContext from '@docusaurus/useDocusaurusContext';
import Layout from '@theme/Layout';
import HomepageFeatures from '@site/src/components/HomepageFeatures';

import Heading from '@theme/Heading';
import styles from "./index.module.css"
import Chatbot from '../components/ChatBot';


function HomepageHeader() {
  const {siteConfig} = useDocusaurusContext();
  return (
    <header className={clsx('hero hero--primary', styles.heroBanner)}>
      <div className="container">
        <Heading as="h1" className="hero__title">
          {/* Ensure your docusaurus.config.js title is set to "Physical AI" */}
          {siteConfig.title} 
        </Heading>
        <p className="hero__subtitle">
          Bridging the gap between digital brains and physical bodies.
        </p>
        <div className={styles.buttons}>
          <Link
            className="button button--secondary button--lg"
            to="/docs/module1/overview">
            Start Module 1: The Nervous System 
          </Link>
        </div>
      </div>
    </header> 
  );
}

export default function Home() {
  const {siteConfig} = useDocusaurusContext();
  return (
    <Layout
      title={`Course: ${siteConfig.title}`}
      description="Master Physical AI, ROS 2, and Humanoid Robotics">
      <HomepageHeader />
      <main>
        <HomepageFeatures />
      </main>
      <Chatbot/>
    </Layout>
  );
}