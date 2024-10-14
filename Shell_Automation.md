## Automating the cloudwatch agent install on EC2 and sending custom metrics to cloudwatch console.

```
#!/bin/bash

install_cloudwatch_agent() {
  local region="$1"
  local config_url="$2"

  # Step 1: Install the CloudWatch Agent
  echo "Installing CloudWatch Agent..."
  sudo yum install -y amazon-cloudwatch-agent

  # Step 2: Download the configuration from S3 (if provided)
  if [[ -n "$config_url" ]]; then
    echo "Fetching CloudWatch Agent configuration from $config_url..."
    aws s3 cp "$config_url" /opt/aws/amazon-cloudwatch-agent/etc/amazon-cloudwatch-agent.json
  fi

  # Step 3: Start the CloudWatch Agent
  echo "Starting CloudWatch Agent..."
  sudo /opt/aws/amazon-cloudwatch-agent/bin/amazon-cloudwatch-agent-ctl \
    -a start -m ec2 \
    -c file:/opt/aws/amazon-cloudwatch-agent/etc/amazon-cloudwatch-agent.json \
    -s

  echo "CloudWatch Agent started in region: $region"
}

# Example Usage
install_cloudwatch_agent "us-east-1" "s3://mybucket/config/amazon-cloudwatch-agent.json"
```
