-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jul 04, 2023 at 02:21 AM
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
-- Database: `lib_l200210056`
--

-- --------------------------------------------------------

--
-- Table structure for table `akun`
--

CREATE TABLE `akun` (
  `username` varchar(100) NOT NULL,
  `nama` varchar(200) DEFAULT NULL,
  `passwords` varchar(200) DEFAULT NULL,
  `roles` set('staff','pengguna') DEFAULT NULL,
  `status_akun` set('aktif','tidak aktif') DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `akun`
--

INSERT INTO `akun` (`username`, `nama`, `passwords`, `roles`, `status_akun`) VALUES
('admin', 'Ngab Admin', '21232f297a57a5a743894a0e4a801fc3', 'staff', 'aktif'),
('contoh', 'Pak Contoh', '4553eb3ff328b4868a7a1e6e53cd28b4', 'pengguna', 'aktif'),
('iniTest', 'Brando', 'd8578edf8458ce06fbc5bb76a58c5ca4', 'pengguna', 'aktif'),
('kaela', 'Kaela Kovalskia', '8fff4eeb530b4c7ed0c0cdebbea77bf6', 'staff', 'aktif'),
('kaela69', 'Mbak Kovalskia', '76d80224611fc919a5d54f0ff9fba446', 'pengguna', 'aktif'),
('kitsune', 'Kitsunee', '832a4c18fc9c6caef9f8cc11ed1afb6e', 'pengguna', 'aktif'),
('moona', 'Hoshinova', '962012d09b8170d912f0669f6d7d9d07', 'pengguna', 'aktif'),
('tes', 'Tes', '098f6bcd4621d373cade4e832627b4f6', 'pengguna', 'aktif'),
('tes1', 'tes1', 'fa3fb6e0dccc657b57251c97db271b05', 'pengguna', 'aktif'),
('test1', 'test123', '098f6bcd4621d373cade4e832627b4f6', 'pengguna', 'aktif');

-- --------------------------------------------------------

--
-- Table structure for table `akun_has_buku`
--

CREATE TABLE `akun_has_buku` (
  `akun_username` varchar(100) NOT NULL,
  `buku_id_buku` varchar(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `akun_has_buku`
--

INSERT INTO `akun_has_buku` (`akun_username`, `buku_id_buku`) VALUES
('kaela', 'CS-1337'),
('kaela', 'CS-526'),
('kaela', 'CS-532');

-- --------------------------------------------------------

--
-- Table structure for table `buku`
--

CREATE TABLE `buku` (
  `id_buku` varchar(10) NOT NULL,
  `katalog_id_katalog` varchar(10) NOT NULL,
  `judul` varchar(200) DEFAULT NULL,
  `pengarang` varchar(200) DEFAULT NULL,
  `penerbit` varchar(200) DEFAULT NULL,
  `tahun_terbit` int(4) UNSIGNED DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `buku`
--

INSERT INTO `buku` (`id_buku`, `katalog_id_katalog`, `judul`, `pengarang`, `penerbit`, `tahun_terbit`) VALUES
('CS-1337', 'KOMP-1337', 'Belajar Pemrograman dan Hacking Menggunakan Python', 'Wardana', 'Elex Media Komputindo', 2019),
('CS-4343', 'KOMP-1337', 'Praktikum Sistem Basis Data', 'Fatah Yasin, Yogiek Indra, Endang Wahyu, Yudi Wahyu, Fendy', 'Muhammadiyah University Press', 2023),
('CS-523', 'KOMP-1337', 'Buku Ilmu Komputer', 'Louis', 'Gramed', 2019),
('CS-524', 'KOMP-1337', 'Buku Sains Komputer', 'Emma', 'Gramed', 2020),
('CS-525', 'KOMP-1337', 'Buku Teknologi Informasi', 'Noah', 'Gramed', 2021),
('CS-526', 'KOMP-1337', 'Buku Jaringan Komputer', 'Olivia', 'Gramed', 2018),
('CS-528', 'KOMP-1337', 'Buku Rekayasa Perangkat Lunak', 'Ava', 'Gramed', 2017),
('CS-529', 'KOMP-1337', 'Buku Keamanan Komputer', 'Mia', 'Gramed', 2023),
('CS-530', 'KOMP-1337', 'Buku Pemrograman Web', 'Noah', 'Gramed', 2016),
('CS-531', 'KOMP-1337', 'Buku Sistem Operasi', 'Olivia', 'Gramed', 2024),
('CS-532', 'KOMP-1337', 'Buku Basis Data', 'Liam', 'Gramed', 2015),
('CS-533', 'KOMP-1337', 'Buku Algoritma', 'Ava', 'Gramed', 2025),
('CS-777', 'KOMP-1337', 'Cara cepat menjadi programmer dalam 1 jam', 'Jack', 'Kompas', 2023),
('CS-7878', 'KOMP-1337', 'Cara cepat jadi hengker', 'Odin', 'Gramed', 2023);

-- --------------------------------------------------------

--
-- Table structure for table `katalog`
--

CREATE TABLE `katalog` (
  `id_katalog` varchar(10) NOT NULL,
  `nomor_rak` varchar(100) DEFAULT NULL,
  `lokasi_rak` varchar(100) DEFAULT NULL,
  `jenis` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `katalog`
--

INSERT INTO `katalog` (`id_katalog`, `nomor_rak`, `lokasi_rak`, `jenis`) VALUES
('KOMP-1337', 'A251', 'Gedung A - Lantai 2', 'Non Fiksi');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `akun`
--
ALTER TABLE `akun`
  ADD PRIMARY KEY (`username`);

--
-- Indexes for table `akun_has_buku`
--
ALTER TABLE `akun_has_buku`
  ADD PRIMARY KEY (`akun_username`,`buku_id_buku`),
  ADD KEY `akun_has_buku_FKIndex1` (`akun_username`),
  ADD KEY `akun_has_buku_FKIndex2` (`buku_id_buku`);

--
-- Indexes for table `buku`
--
ALTER TABLE `buku`
  ADD PRIMARY KEY (`id_buku`),
  ADD KEY `buku_FKIndex1` (`katalog_id_katalog`);

--
-- Indexes for table `katalog`
--
ALTER TABLE `katalog`
  ADD PRIMARY KEY (`id_katalog`);

--
-- Constraints for dumped tables
--

--
-- Constraints for table `akun_has_buku`
--
ALTER TABLE `akun_has_buku`
  ADD CONSTRAINT `akun_has_buku_ibfk_1` FOREIGN KEY (`akun_username`) REFERENCES `akun` (`username`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  ADD CONSTRAINT `akun_has_buku_ibfk_2` FOREIGN KEY (`buku_id_buku`) REFERENCES `buku` (`id_buku`) ON DELETE NO ACTION ON UPDATE NO ACTION;

--
-- Constraints for table `buku`
--
ALTER TABLE `buku`
  ADD CONSTRAINT `buku_ibfk_1` FOREIGN KEY (`katalog_id_katalog`) REFERENCES `katalog` (`id_katalog`) ON DELETE NO ACTION ON UPDATE NO ACTION;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
