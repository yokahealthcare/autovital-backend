-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Nov 11, 2023 at 04:27 PM
-- Server version: 10.4.28-MariaDB
-- PHP Version: 8.2.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `autovital2`
--

-- --------------------------------------------------------

--
-- Table structure for table `account`
--

CREATE TABLE `account` (
  `uid` varchar(100) NOT NULL,
  `username` varchar(100) NOT NULL,
  `password` varchar(100) NOT NULL,
  `phone` varchar(100) NOT NULL,
  `email` varchar(100) NOT NULL,
  `verified` int(11) DEFAULT 0
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `account`
--

INSERT INTO `account` (`uid`, `username`, `password`, `phone`, `email`, `verified`) VALUES
('4b18f586-ade1-4d76-935f-5cbeff94697f', 'erwinyonata', '$2b$12$fWwsdef3L0Xd8mq0lM2OXelo/3Qz/wFWlz9nFQlb5pQ.ipAiOPrFi', '092319342', 'erwinwingyonata@gmail.com', 1);

-- --------------------------------------------------------

--
-- Table structure for table `air_filter`
--

CREATE TABLE `air_filter` (
  `afid` varchar(100) NOT NULL,
  `name` varchar(100) NOT NULL,
  `last_change` date NOT NULL,
  `aid` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `air_filter`
--

INSERT INTO `air_filter` (`afid`, `name`, `last_change`, `aid`) VALUES
('a2b9bae5-ece3-48da-996d-d3a2066007bc', 'Winder Premium', '2023-09-01', '4486742a-6041-4e12-be4d-59c6a4a944fa'),
('bf529b2c-8ca1-4bf5-b26b-5afbe5ed6270', 'Winder Premium', '2023-09-01', '4632e84b-9599-4cec-99a2-b662af1b3e85');

-- --------------------------------------------------------

--
-- Table structure for table `automotive`
--

CREATE TABLE `automotive` (
  `aid` varchar(100) NOT NULL,
  `name` varchar(100) NOT NULL,
  `plate` varchar(100) NOT NULL,
  `vin` varchar(100) NOT NULL,
  `distance` int(11) NOT NULL,
  `cid` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `automotive`
--

INSERT INTO `automotive` (`aid`, `name`, `plate`, `vin`, `distance`, `cid`) VALUES
('4486742a-6041-4e12-be4d-59c6a4a944fa', 'ferrari', 'L2110EY', '1312HDFKSA832024', 3204, '2'),
('4632e84b-9599-4cec-99a2-b662af1b3e85', 'ferrari', 'L2110EY', '1312HDFKSA832024', 3204, '2');

-- --------------------------------------------------------

--
-- Table structure for table `breakpad`
--

CREATE TABLE `breakpad` (
  `bpid` varchar(100) NOT NULL,
  `name` varchar(100) NOT NULL,
  `last_change` date NOT NULL,
  `aid` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `breakpad`
--

INSERT INTO `breakpad` (`bpid`, `name`, `last_change`, `aid`) VALUES
('2316490d-bc24-4e48-afa9-5deb8ffc3994', 'Stop Car', '2023-05-03', '4632e84b-9599-4cec-99a2-b662af1b3e85'),
('8aeadebf-5951-4518-958c-4d1561cd7b0e', 'Stop Car', '2023-05-03', '4486742a-6041-4e12-be4d-59c6a4a944fa');

-- --------------------------------------------------------

--
-- Table structure for table `car`
--

CREATE TABLE `car` (
  `cid` varchar(100) NOT NULL,
  `brand` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  `thumbnail` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `car`
--

INSERT INTO `car` (`cid`, `brand`, `model`, `thumbnail`) VALUES
('1', 'Toyota', 'Camry', 'https://imgd.aeplcdn.com/0X0/n/cw/ec/110233/camry-exterior-right-front-three-quarter-3.jpeg'),
('10', 'Subaru', 'Impreza', 'https://otoklix-production.s3.amazonaws.com/uploads/2022/12/subaru-impreza.jpg'),
('2', 'Honda', 'Civic', 'https://www.kba.one/files/images/20210730-b68d069167d64751bf08d7e2a18007ed-750x420.jpg'),
('3', 'Ford', 'Focus', 'https://www.topgear.com/sites/default/files/2022/04/51951944136_a4826c854b_k.jpg'),
('4', 'Chevrolet', 'Malibu', 'https://www.motortrend.com/uploads/2022/10/2023-Chevrolet-Malibu-RS-30.jpg'),
('5', 'Volkswagen', 'Jetta', 'https://cdn.jdpower.com/JDPA_2020%20Volkswagen%20Jetta%20GLI%20Pure%20Gray%20Front%20View.jpg'),
('6', 'Nissan', 'Altima', 'https://cars.usnews.com/static/images/Auto/izmo/i157546817/2020_nissan_altima_angularfront.jpg'),
('7', 'Hyundai', 'Elantra', 'https://cdn.motor1.com/images/mgl/xqgZLP/s1/2022-hyundai-elantra-n-exterior-front-quarter.jpg'),
('8', 'Kia', 'Forte', 'https://di-uploads-pod35.dealerinspire.com/kiaofriverdale/uploads/2022/09/2023-Kia-Forte.png'),
('9', 'Mazda', 'Mazda3', 'https://cdn.motor1.com/images/mgl/kN9Ex/s1/2021-mazda3-update-in-japan.jpg');

-- --------------------------------------------------------

--
-- Table structure for table `fuel_filter`
--

CREATE TABLE `fuel_filter` (
  `ffid` varchar(100) NOT NULL,
  `name` varchar(100) NOT NULL,
  `last_change` date NOT NULL,
  `aid` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `fuel_filter`
--

INSERT INTO `fuel_filter` (`ffid`, `name`, `last_change`, `aid`) VALUES
('e6a5cb5c-61aa-486b-9692-2a52d6466f78', 'Peroz Utips', '2023-01-01', '4632e84b-9599-4cec-99a2-b662af1b3e85'),
('fd4301b9-dc27-496f-bdb1-f061ed149844', 'Peroz Utips', '2023-01-01', '4486742a-6041-4e12-be4d-59c6a4a944fa');

-- --------------------------------------------------------

--
-- Table structure for table `oil`
--

CREATE TABLE `oil` (
  `oid` varchar(100) NOT NULL,
  `name` varchar(100) NOT NULL,
  `last_change` date NOT NULL,
  `aid` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `oil`
--

INSERT INTO `oil` (`oid`, `name`, `last_change`, `aid`) VALUES
('1e5297e8-73f7-48f0-8066-22d4142724b4', 'GS Astra', '2023-11-02', '4486742a-6041-4e12-be4d-59c6a4a944fa'),
('d167aa1f-0874-42d5-bc23-8a58c9bbfee0', 'GS Astra', '2023-11-02', '4632e84b-9599-4cec-99a2-b662af1b3e85');

-- --------------------------------------------------------

--
-- Table structure for table `oil_filter`
--

CREATE TABLE `oil_filter` (
  `ofid` varchar(100) NOT NULL,
  `name` varchar(100) NOT NULL,
  `last_change` date NOT NULL,
  `aid` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `oil_filter`
--

INSERT INTO `oil_filter` (`ofid`, `name`, `last_change`, `aid`) VALUES
('0e3bdbf8-8d26-4bd9-a61c-e32ade10a862', 'Loper Bear', '2023-04-09', '4632e84b-9599-4cec-99a2-b662af1b3e85'),
('a3adc429-70aa-40f4-aa27-dd575bc99660', 'Loper Bear', '2023-04-09', '4486742a-6041-4e12-be4d-59c6a4a944fa');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `account`
--
ALTER TABLE `account`
  ADD PRIMARY KEY (`uid`);

--
-- Indexes for table `air_filter`
--
ALTER TABLE `air_filter`
  ADD PRIMARY KEY (`afid`),
  ADD KEY `aid` (`aid`);

--
-- Indexes for table `automotive`
--
ALTER TABLE `automotive`
  ADD PRIMARY KEY (`aid`),
  ADD KEY `cid` (`cid`);

--
-- Indexes for table `breakpad`
--
ALTER TABLE `breakpad`
  ADD PRIMARY KEY (`bpid`),
  ADD KEY `aid` (`aid`);

--
-- Indexes for table `car`
--
ALTER TABLE `car`
  ADD PRIMARY KEY (`cid`);

--
-- Indexes for table `fuel_filter`
--
ALTER TABLE `fuel_filter`
  ADD PRIMARY KEY (`ffid`),
  ADD KEY `aid` (`aid`);

--
-- Indexes for table `oil`
--
ALTER TABLE `oil`
  ADD PRIMARY KEY (`oid`),
  ADD KEY `aid` (`aid`);

--
-- Indexes for table `oil_filter`
--
ALTER TABLE `oil_filter`
  ADD PRIMARY KEY (`ofid`),
  ADD KEY `aid` (`aid`);

--
-- Constraints for dumped tables
--

--
-- Constraints for table `air_filter`
--
ALTER TABLE `air_filter`
  ADD CONSTRAINT `air_filter_ibfk_1` FOREIGN KEY (`aid`) REFERENCES `automotive` (`aid`);

--
-- Constraints for table `automotive`
--
ALTER TABLE `automotive`
  ADD CONSTRAINT `automotive_ibfk_1` FOREIGN KEY (`cid`) REFERENCES `car` (`cid`);

--
-- Constraints for table `breakpad`
--
ALTER TABLE `breakpad`
  ADD CONSTRAINT `breakpad_ibfk_1` FOREIGN KEY (`aid`) REFERENCES `automotive` (`aid`);

--
-- Constraints for table `fuel_filter`
--
ALTER TABLE `fuel_filter`
  ADD CONSTRAINT `fuel_filter_ibfk_1` FOREIGN KEY (`aid`) REFERENCES `automotive` (`aid`);

--
-- Constraints for table `oil`
--
ALTER TABLE `oil`
  ADD CONSTRAINT `oil_ibfk_1` FOREIGN KEY (`aid`) REFERENCES `automotive` (`aid`);

--
-- Constraints for table `oil_filter`
--
ALTER TABLE `oil_filter`
  ADD CONSTRAINT `oil_filter_ibfk_1` FOREIGN KEY (`aid`) REFERENCES `automotive` (`aid`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
